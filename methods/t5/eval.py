#!/usr/bin/env python3
#% python3 evaluator.py -qa datasets/csqa/questions.jsonl -p predictions.csv -o metrics.json
# python eval.py -qa datasets/csqa/dev_rand_split.jsonl -p outputs/csqa/dev.csv -o metrics.json
import csv
from typing import *
import logging
import os
import sys
import json
import argparse

EXIT_STATUS_ANSWERS_MALFORMED = 1
EXIT_STATUS_PREDICTIONS_MALFORMED = 2
EXIT_STATUS_PREDICTIONS_EXTRA = 3
EXIT_STATUS_PREDICTION_MISSING = 4


def calculate_accuracy(question_answers: Dict[str, str], predictions: Dict[str, List[str]]) -> float:
    score = 0.0

    for question_id, answer in question_answers.items():
        try:
            predictions_for_q = predictions[question_id]
        except KeyError:
            logging.error("Missing prediction for question '%s'.", question_id)
            sys.exit(EXIT_STATUS_PREDICTION_MISSING)

        if answer.strip() == predictions_for_q[0].strip():
            score += 1.0 / len(predictions_for_q)

        del predictions[question_id]

    if len(predictions) > 0:
        logging.error("Found %d extra predictions, for example: %s", len(predictions),
                      ", ".join(list(predictions.keys())[:3]))
        sys.exit(EXIT_STATUS_PREDICTIONS_EXTRA)

    return score / len(question_answers)


def read_answers(filename: str) -> Dict[str, str]:
    answers = {}

    with open(filename, "rt", encoding="UTF-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            try:
                record = json.loads(line)
            except ValueError as e:
                logging.error("Error while reading file %s: %s", filename, e)
                sys.exit(EXIT_STATUS_ANSWERS_MALFORMED)
            question_id = record["id"]
            answer_key = record["answerKey"]
            answer = ""
            for answer_string in record["question"]["choices"]:
                if answer_string["label"] == answer_key:
                    answer = answer_string["text"]

            if question_id in answers:
                logging.error("Key %s repeated in %s", question_id, filename)
                sys.exit(EXIT_STATUS_ANSWERS_MALFORMED)
            answers[question_id] = answer

    if len(answers) == 0:
        logging.error("No answers found in file %s", filename)
        sys.exit(EXIT_STATUS_ANSWERS_MALFORMED)

    return answers


def read_predictions(filename: str) -> Dict[str, List[str]]:
    predictions = {}

    with open(filename, "rt", encoding="UTF-8", errors="replace") as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                try:
                    question_id = row[0]
                    prediction_raw = row[1]
                except IndexError as e:
                    logging.error("Error reading value from CSV file %s on line %d: %s", filename, reader.line_num, e)
                    sys.exit(EXIT_STATUS_PREDICTIONS_MALFORMED)

                if question_id in predictions:
                    logging.error("Key %s repeated in file %s on line %d", question_id, filename, reader.line_num)
                    sys.exit(EXIT_STATUS_PREDICTIONS_MALFORMED)

                if question_id == "":
                    logging.error("Key is empty in file %s on line %d", filename, reader.line_num)
                    sys.exit(EXIT_STATUS_PREDICTIONS_MALFORMED)

                prediction = prediction_raw.split(";")
                predictions[question_id] = prediction

        except csv.Error as e:
            logging.error('file %s, line %d: %s', filename, reader.line_num, e)
            sys.exit(EXIT_STATUS_PREDICTIONS_MALFORMED)

    return predictions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground_truth_labels_dir", type=str, default="data_dir/riddle_sense")
    parser.add_argument("--predicted_labels_dir", type=str, required=True)

    args = parser.parse_known_args()[0]

    test_ground_truth_labels_file = os.path.join(args.ground_truth_labels_dir, "rs_test.jsonl")
    test_predicted_labels_file = os.path.join(args.predicted_labels_dir, "test.csv")
    test_question_answers = read_answers(test_ground_truth_labels_file)
    test_predictions = read_predictions(test_predicted_labels_file)

    test_out = "Test Accuracy score = " + str(calculate_accuracy(test_question_answers, test_predictions)) + "\n"
    print(test_out)

    dev_ground_truth_labels_file = os.path.join(args.ground_truth_labels_dir, "rs_dev.jsonl")
    dev_predicted_labels_file = os.path.join(args.predicted_labels_dir, "dev.csv")
    dev_question_answers = read_answers(dev_ground_truth_labels_file)
    dev_predictions = read_predictions(dev_predicted_labels_file)

    dev_out = "Dev Accuracy score = " + str(calculate_accuracy(dev_question_answers, dev_predictions)) + "\n"
    print(dev_out)

if __name__ == '__main__':
    main()
