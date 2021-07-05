from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
import json
import logging
from tqdm import tqdm
import os
logger = logging.getLogger(__name__)


class InputExample(object):

    def __init__(self, example_id, question, contexts, endings, label=None):
        """Construct an instance."""
        self.example_id = example_id
        self.question = question
        self.contexts = contexts
        self.endings = endings
        self.label = label


class DataProcessor:
    """Base class for data converters for sequence classification data sets."""

    def get_train_examples(self, data_dir, num_choices):
        """Gets a collection of `InputExample`s for the train set."""
        raise NotImplementedError()

    def get_dev_examples(self, data_dir, num_choices):
        """Gets a collection of `InputExample`s for the dev set."""
        raise NotImplementedError()

    def get_test_examples(self, data_dir, num_choices):
        """Gets a collection of `InputExample`s for prediction."""
        raise NotImplementedError()

    def get_labels(self, num_choices):
        """Gets the list of labels for this data set."""
        raise NotImplementedError()

    @classmethod
    def _read_json(cls, input_file):
        with open(input_file, "r", encoding="utf-8") as fin:
            lines = fin.readlines()
            return lines


class RiddleSenseProcessor(DataProcessor):
    """Processor for the riddlesense data set."""

    TRAIN_FILE_NAME = 'train.jsonl'
    DEV_FILE_NAME = 'rs_dev.jsonl'
    TEST_FILE_NAME = 'rs_test.jsonl'

    def get_train_examples(self, data_dir, num_choices=5):
        train_file_name = self.TRAIN_FILE_NAME
        return self._create_examples(self._read_json(os.path.join(data_dir, train_file_name)), 'train', num_choices=num_choices)

    def get_dev_examples(self, data_dir, num_choices=5):
        dev_file_name = self.DEV_FILE_NAME
        return self._create_examples(self._read_json(os.path.join(data_dir, dev_file_name)), 'dev', num_choices=num_choices)

    def get_test_examples(self, data_dir, num_choices):
        test_file_name = self.TEST_FILE_NAME
        return self._create_examples(self._read_json(os.path.join(data_dir, test_file_name)), 'test', num_choices=num_choices)

    def get_labels(self, num_choices):
        """See base class."""
        return [str(i) for i in range(1,num_choices+1)]

    def _create_examples(self, lines, type, num_choices):
        """Creates examples for the training and validation sets."""

        # There are two types of labels. They should be normalized
        def normalize(truth):
            if truth in [str(i) for i in range(1,num_choices+1)]:
                return int(truth)
            else:
                logger.info("truth ERROR! %s", str(truth))
                return None

        def convert_ABC_to_123(s):
            assert len(s) == 1 and s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            return ord(s) - 65 + 1

        examples = []
        # we deleted example which has more than or less than four choices
        for line in tqdm(lines, desc="read arc data"):
            data_raw = json.loads(line.strip("\n"))
            if len(data_raw["question"]["choices"]) != num_choices:
                print(num_choices)
                print(len(data_raw["question"]["choices"]))
            assert len(data_raw["question"]["choices"]) == num_choices
            truth = str(convert_ABC_to_123(data_raw["answerKey"]))
            assert truth != "None" or type == "test"
            question_choices = data_raw["question"]
            question = question_choices["stem"]
            id = data_raw["id"]
            options = question_choices["choices"]
            if len(options) == num_choices:
                examples.append(
                    InputExample(
                        example_id=id,
                        question=question,
                        contexts=[" " for i in range(num_choices)],
                        endings=[options[i]["text"] for i in range(num_choices)],
                        label=truth,
                    )
                )
        if type == "train":
            assert len(examples) > 1
            assert examples[0].label is not None
        logger.info("len examples: %s}", str(len(examples)))
        return examples


class RiddleSenseDataset(Dataset):
    def __init__(self, tokenizer, data_dir, type_path, max_len=512):
        self.data_dir = data_dir
        self.type_path = type_path
        self.max_len = max_len
        self.tokenizer = tokenizer
        self.inputs = []
        self.targets = []

        self.proc = RiddleSenseProcessor()
        self._build()

    def __getitem__(self, index):
        source_ids = self.inputs[index]["input_ids"].squeeze()
        target_ids = self.targets[index]["input_ids"].squeeze()
        src_mask = self.inputs[index]["attention_mask"].squeeze()  # might need to squeeze
        target_mask = self.targets[index]["attention_mask"].squeeze()  # might need to squeeze

        return {"source_ids": source_ids, "source_mask": src_mask, "target_ids": target_ids, "target_mask": target_mask}

    def __len__(self):
        return len(self.inputs)

    def _build(self):
        if self.type_path == 'train':
            examples = self.proc.get_train_examples(self.data_dir)
        else:
            examples = self.proc.get_dev_examples(self.data_dir)

        for example in examples:
            self._create_features(example)

    def _create_features(self, example):
        input_ = example.question
        options = ['(%s) %s' % (i, option) for i, option in zip(['A','B','C','D','E'], example.endings)]
        input_ = "%s \\n %s" % (input_, " ".join(options))
        target = "%s" % str(example.endings[int(example.label)-1])

        tokenized_inputs = self.tokenizer.batch_encode_plus(
            [input_], max_length=self.max_len, pad_to_max_length=True, return_tensors="pt", truncation=True
        )

        tokenized_targets = self.tokenizer.batch_encode_plus(
            [target], max_length=int(self.max_len / 4), pad_to_max_length=True, return_tensors="pt", truncation=True
        )

        self.inputs.append(tokenized_inputs)
        self.targets.append(tokenized_targets)
