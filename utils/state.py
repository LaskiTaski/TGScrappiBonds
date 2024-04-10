from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMClientSettings(StatesGroup):
    QuotingState = State()
    EndState = State()
    NominalState = State()
    MarketState = State()
    FrequencyState = State()
    DaysState = State()
    QualificationState = State()