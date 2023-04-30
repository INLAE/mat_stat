from Decision import Decision
from IEntity import IEntity


class DecisionQuery(Decision):
    def __init__(self, title: str, positive: Decision, negative: Decision):
        self.title = title
        self.positive = positive
        self.negative = negative

    def evaluate(self, entity: IEntity):
        if entity.set_title_gui(self.title):
            self.positive.evaluate(entity)
        else:
            self.negative.evaluate(entity)