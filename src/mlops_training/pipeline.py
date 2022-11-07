import mlflow
from metaflow import FlowSpec, step


class FhPFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.ingest)

    @step
    def ingest(self):

        self.next(self.split)

    @step
    def split(self):
        self.next(self.transform)

    @step
    def transform(self):
        self.next(self.train)

    @step
    def train(self):
        self.next(self.evaluate)

    @step
    def evaluate(self):
        self.next(self.end)

    @step
    def end(self):
        pass


def main():
    with mlflow.start_run():
        FhPFlow()
