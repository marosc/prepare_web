import json as _json
import os as _os

import pandas as _pd

from config import user_config as _ucnf

EXPERIMENT_TIMES = {}
# TF_CPP_MIN_LOG_LEVEL = _ucnf.TF_CPP_MIN_LOG_LEVEL
# CUDA_VISIBLE_DEVICES = _ucnf.CUDA_VISIBLE_DEVICES

EXPERIMENT_NAME = _ucnf.EXPERIMENT_NAME

LOAD_STOCKS = _ucnf.LOAD_STOCKS
MERGE_STOCKS = _ucnf.MERGE_STOCKS

SIMULATE_ADVICES = _ucnf.SIMULATE_ADVICES
SIMULATE_TRADES = _ucnf.SIMULATE_TRADES
SIMULATE_ACTIONS = _ucnf.SIMULATE_ACTIONS

CREATE_MODELS_FOR_STOCK_NAMES = _ucnf.CREATE_MODELS_FOR_STOCK_NAMES
HOW_MANY_MODELS = _ucnf.HOW_MANY_MODELS
MODEL_INDEX_OFFSET = _ucnf.MODEL_INDEX_OFFSET

USER_CONFIG_FILE = "user_config.json"
FULL_CONFIG_FILE = "full_config.json"

EXPERIMENT_DATA_PATH = _ucnf.EXPERIMENT_DATA_PATH

# assert not _os.path.exists(EXPERIMENT_DATA_PATH), "experiment "+EXPERIMENT_NAME+" already exists!!! chose different name"

BASE_STOCK_TXT_FILES_PATH = _ucnf.BASE_STOCK_TXT_FILES_PATH  # leave blank for default EXPERIMENT_DATA_PATH/stocks/
BASE_METADATA_FILES_PATH = _ucnf.BASE_METADATA_FILES_PATH  # leave blank for default EXPERIMENT_DATA_PATH/metadata/
BASE_MATRICES_FILES_PATH = _ucnf.BASE_MATRICES_FILES_PATH  # leave blank for default EXPERIMENT_DATA_PATH/matrices/
BASE_MODELS_FILES_PATH = _ucnf.BASE_MODELS_FILES_PATH  # leave blank for default EXPERIMENT_DATA_PATH/models/
BASE_PREDICTIONS_FILES_PATH = _ucnf.BASE_PREDICTIONS_FILES_PATH  # leave blank for default EXPERIMENT_DATA_PATH/predictions/
BASE_BACKTEST_DATA_DIRECTORY_PATH = _ucnf.BASE_BACKTEST_DATA_DIRECTORY_PATH
BASE_SIMULATION_INPUT_ACTION_FILES_PATH = _ucnf.BASE_SIMULATION_INPUT_ACTION_FILES_PATH # leave blank for default EXPERIMENT_DATA_PATH/simulation/input/actions/
BASE_SIMULATION_INPUT_TRADES_FILES_PATH = _ucnf.BASE_SIMULATION_INPUT_TRADES_FILES_PATH # leave blank for default EXPERIMENT_DATA_PATH/simulation/input/trades/
BASE_SIMULATION_INPUT_ADVICES_FILES_PATH = _ucnf.BASE_SIMULATION_INPUT_ADVICES_FILES_PATH # leave blank for default EXPERIMENT_DATA_PATH/simulation/input/advices/
BASE_SIMULATION_METADATA_FILES_PATH = _ucnf.BASE_SIMULATION_METADATA_FILES_PATH   # leave blank for default EXPERIMENT_DATA_PATH/simulation/metadata/
BASE_SIMULATION_BALANCE_DIRECTORY_PATH = _ucnf.BASE_SIMULATION_BALANCE_DIRECTORY_PATH  # leave blank for default EXPERIMENT_DATA_PATH/simulation/balance/
SIMULATION_BALANCE_DATA_DIRECTORY_NAME = _ucnf.SIMULATION_BALANCE_DATA_DIRECTORY_NAME

_os.environ['MPLCONFIGDIR'] = EXPERIMENT_DATA_PATH + "temp/"

EXPERIMENT_PREPARATION = "preparation"
EXPERIMENT_MERGE_DATA= "merge_data"
EXPERIMENT_TRAINING = "training"
EXPERIMENT_EMULATION = "emulation"
EXPERIMENT_BACKTESTING = "backtesting"
EXPERIMENT_SIMULATION = "simulation"
EXPERIMENT_EXECUTED = {
    EXPERIMENT_PREPARATION: 0,
    EXPERIMENT_MERGE_DATA: 0,
    EXPERIMENT_TRAINING: 0,
    EXPERIMENT_EMULATION: 0,
    EXPERIMENT_BACKTESTING: 0,
    EXPERIMENT_SIMULATION: 0
}


INPUT_FILTER_TIME_START = _ucnf.INPUT_FILTER_TIME_START
INPUT_FILTER_TIME_END = _ucnf.INPUT_FILTER_TIME_END
INPUT_FILTER_DATE_START = _ucnf.INPUT_FILTER_DATE_START
INPUT_FILTER_DATE_END = _ucnf.INPUT_FILTER_DATE_END

TRAINING_START_DAY = _pd.to_datetime(_ucnf.TRAINING_START_DAY).timestamp()
TRAINING_END_DAY = _pd.to_datetime(_ucnf.TRAINING_END_DAY).timestamp()
TESTING_START_DAY = _pd.to_datetime(_ucnf.TESTING_START_DAY).timestamp()
TESTING_END_DAY = _pd.to_datetime(_ucnf.TESTING_END_DAY).timestamp()
MIN_CANDLES_TO_INCLUDE_STOCK = _ucnf.MIN_CANDLES_TO_INCLUDE_STOCK

BACKTESTING_START_DAY = _pd.to_datetime(_ucnf.BACKTESTING_START_DAY).timestamp()
BACKTESTING_END_DAY = _pd.to_datetime(_ucnf.BACKTESTING_END_DAY).timestamp()

# skip first NaN rows in calculated indicators ohlc in indicators.csv, now based on EMA50
P_SKIP_FIRST_ROWS = 49

# OHLC column names used for dataframes and csv
OPEN_COL = "open"
CLOSE_COL = "close"
HIGH_COL = "high"
LOW_COL = "low"
VOLUME_BASE_COL = "volume_base"
DATE_COL = "date"
UNIX_COL = "unix"

OHLCV_FILE = "ohlcv.csv"
OHLCV_COLUMNS = [UNIX_COL, DATE_COL, OPEN_COL, HIGH_COL, LOW_COL, CLOSE_COL, VOLUME_BASE_COL]


# Indicators column names used for dataframes and csv
I_BB_BBM = "bb_bbm"
I_BB_BBH = "bb_bbh"
I_BB_BBL = "bb_bbl"
I_BB_BBHI = "bb_bbhi"
I_BB_BBLI = "bb_bbli"
I_KCH_PERCENTAGE = "kch_percentage"
I_KCH_HIGH = "kch_high"
I_KCH_LOW = "kch_low"
I_KCH_MID = "kch_mid"
I_KCH_HIGH_SQUEEZE = "kch_high_squeeze"
I_KCH_LOW_SQUEEZE = "kch_low_squeeze"
I_KCH_MID_SQUEEZE = "kch_mid_squeeze"
I_KCH_TR_SQUEEZE = "kch_tr_squeeze"
I_SQUEEZE = "squeeze"
I_POCKET_PIVOT = "pocket_pivot"
I_RSI = "rsi"
I_ROC = "roc"
I_TSI = "tsi"
I_MFI = "mfi"
I_VWAP = "vwap"
I_ATR = "atr"
I_ATR_NORM = "atr_norm"
I_ADX = "adx"
I_OBV = "obv"
I_CMF = "cmf"
I_AROON_UP = "aroon_up"
I_AROON = "aroon"
I_AROON_DOWN = "aroon_down"
I_SMA = "sma"
I_EMA20 = "ema20"
I_EMA50 = "ema50"
I_EMA100 = "ema100"
I_EMA200 = "ema200"
I_MACD_DIFF = "macd_diff"
I_MACD = "macd"
I_MACD_SIGNAL = "macd_signal"
I_CUMSUM_VOLUME = "cumsum_volume"
I_SMA_VOLUME = "sma_volume"

# calc indicators parameters
P_BB_WINDOW = 20
P_BB_WINDOW_DEV = 2
P_KCH_WINDOW = 20
P_RSI_WINDOW = 20
P_ROC_WINDOW = 20
P_TSI_WINDOW_FAST = 13
P_TSI_WINDOW_SLOW = 25
P_MFI_WINDOW = 14
P_ATR_WINDOW = 14
P_ADX_WINDOW = 14
P_AROON_WINDOW = 25
P_SMA_WINDOW = 20
P_EMA_WINDOW_20 = 20
P_EMA_WINDOW_50 = 50
P_EMA_WINDOW_100 = 100
P_EMA_WINDOW_200 = 200
P_MACD_WINDOW_SLOW = 26
P_MACD_WINDOW_FAST = 12
P_MACD_WINDOW_SIGN = 9
P_CMF_WINDOW = 14
P_PIVOT_LENGTH = 10
P_PIVOT_SIZE = 1.3
P_VWAP_WINDOW = 14
P_SMA_VOLUME_WINDOW = 50
P_KCH_SQUEEZE_WINDOW = 20
P_KCH_SQUEEZE_ATR_LENGTH = 20
P_KCH_SQUEEZE_MULTIPLIER = 1.5

INDICATORS_FILE = "indicators.csv"
INDICATORS_COLUMNS = [
    UNIX_COL, DATE_COL, OPEN_COL, HIGH_COL, LOW_COL, CLOSE_COL, VOLUME_BASE_COL,
    I_BB_BBM, I_BB_BBH, I_BB_BBL, I_KCH_HIGH, I_KCH_LOW, I_KCH_MID, I_KCH_MID_SQUEEZE,
    I_KCH_TR_SQUEEZE, I_KCH_HIGH_SQUEEZE, I_KCH_LOW_SQUEEZE, I_SQUEEZE, I_RSI, I_ROC,
    I_TSI, I_MFI, I_VWAP, I_ATR, I_ADX, I_OBV, I_SMA_VOLUME, I_POCKET_PIVOT,
    I_CMF, I_AROON_UP, I_AROON, I_AROON_DOWN, I_SMA, I_EMA20, I_EMA50,
    I_MACD_DIFF, I_MACD, I_MACD_SIGNAL
]

# calc normalized indicators
NORMALIZED_INDICATORS_FILE = "normalized.csv"
NORMALIZED_INDICATORS_COLUMNS = [
    UNIX_COL, DATE_COL, OPEN_COL, HIGH_COL, LOW_COL, CLOSE_COL, VOLUME_BASE_COL,
    I_BB_BBM, I_BB_BBH, I_BB_BBL, I_KCH_HIGH, I_KCH_LOW, I_KCH_MID, I_SQUEEZE, I_RSI, I_ROC,
    I_TSI, I_MFI, I_VWAP, I_ATR, I_ADX, I_OBV, I_POCKET_PIVOT,
    I_CMF, I_AROON_UP, I_AROON, I_AROON_DOWN, I_SMA, I_EMA20, I_EMA50,
    I_MACD_DIFF
]


# Renko column names used for dataframes and csv
RENKO_START_UNIX_COL = "start_unix"
RENKO_END_UNIX_COL = "end_unix"
RENKO_START_DATE_COL = "start"
RENKO_END_DATE_COL = "end"
RENKO_BOTTOM_COL = "bottom"
RENKO_TOP_COL = "top"
RENKO_DIRECTION_COL = "direction"
RENKO_FINISHED_COL = "finished"

RENKO_DIRECTION_UP = 1
RENKO_DIRECTION_DOWN = -1
RENKOS_FROM_NORMALIZED_ATR = _ucnf.RENKOS_FROM_NORMALIZED_ATR
RENKO_FINISHED = 1
RENKO_UNFINISHED= 0

RENKOS_FILE = "renkos.csv"
RENKOS_COLUMNS = [RENKO_START_DATE_COL, RENKO_START_UNIX_COL, RENKO_BOTTOM_COL, RENKO_TOP_COL,
                  RENKO_END_DATE_COL, RENKO_END_UNIX_COL, RENKO_DIRECTION_COL]

ALL_RENKOS_FILE = "all_renkos.csv"
ALL_RENKOS_COLUMNS = [RENKO_START_DATE_COL, RENKO_START_UNIX_COL, RENKO_BOTTOM_COL, RENKO_TOP_COL,
                  RENKO_END_DATE_COL, RENKO_END_UNIX_COL, RENKO_DIRECTION_COL, RENKO_FINISHED_COL ]

# Triples column names used for dataframes and csv
TRIPLE_START_UNIX_COL = "start_unix"
TRIPLE_END_UNIX_COL = "end_unix"
TRIPLE_START_DATE_COL = "start"
TRIPLE_END_DATE_COL = "end"
TRIPLE_START_OPEN_COL = "start_open"
TRIPLE_START_HIGH_COL = "start_high"
TRIPLE_START_LOW_COL = "start_low"
TRIPLE_START_CLOSE_COL = "start_close"
TRIPLE_START_VOLUME_COL = "start_volume"
TRIPLE_END_OPEN_COL = "end_open"
TRIPLE_END_HIGH_COL = "end_high"
TRIPLE_END_LOW_COL = "end_low"
TRIPLE_END_CLOSE_COL = "end_close"
TRIPLE_END_VOLUME_COL = "end_volume"
TRIPLE_BOTTOM_COL = "bottom"
TRIPLE_TOP_COL = "top"
TRIPLE_DIRECTION_COL = "direction"
TRIPLE_FINISHED_COL = "finished"

TRIPLE_FINISHED = 1
TRIPLE_UNFINISHED= 0
TRIPLE_DIRECTION_UP_UP = 0.75
TRIPLE_DIRECTION_UP_DOWN = 0.25
TRIPLE_DIRECTION_DOWN_UP = -0.25
TRIPLE_DIRECTION_DOWN_DOWN = -0.75
TRIPLE_INDICATORS_COLS = [I_BB_BBH, I_BB_BBL, I_KCH_HIGH, I_KCH_LOW, I_SQUEEZE, I_RSI,
                          I_ROC, I_TSI, I_MFI, I_VWAP, I_ATR, I_ADX, I_OBV, I_POCKET_PIVOT, I_CMF,
                          I_AROON_UP, I_AROON, I_AROON_DOWN, I_SMA,
                          I_EMA20, I_EMA50, I_MACD_DIFF]

TRIPLES_FILE = "triples.csv"
TRIPLES_COLUMNS = [TRIPLE_START_DATE_COL, TRIPLE_START_UNIX_COL, TRIPLE_END_DATE_COL, TRIPLE_END_UNIX_COL, TRIPLE_DIRECTION_COL, TRIPLE_BOTTOM_COL, TRIPLE_TOP_COL,
                   TRIPLE_START_OPEN_COL, TRIPLE_START_HIGH_COL, TRIPLE_START_LOW_COL, TRIPLE_START_CLOSE_COL, TRIPLE_START_VOLUME_COL,
                   TRIPLE_END_OPEN_COL, TRIPLE_END_HIGH_COL, TRIPLE_END_LOW_COL, TRIPLE_END_CLOSE_COL, TRIPLE_END_VOLUME_COL,
                   I_BB_BBH, I_BB_BBL, I_KCH_HIGH, I_KCH_LOW, I_SQUEEZE, I_RSI,
                   I_ROC, I_TSI, I_MFI, I_VWAP, I_ATR, I_ADX, I_OBV, I_POCKET_PIVOT, I_CMF,
                   I_AROON_UP, I_AROON, I_AROON_DOWN, I_SMA,
                   I_EMA20, I_EMA50, I_MACD_DIFF
                   ]

ALL_TRIPLES_FILE = "all_triples.csv"
ALL_TRIPLES_COLUMNS = [TRIPLE_START_DATE_COL, TRIPLE_START_UNIX_COL, TRIPLE_END_DATE_COL, TRIPLE_END_UNIX_COL,
                       TRIPLE_DIRECTION_COL, TRIPLE_FINISHED_COL, TRIPLE_BOTTOM_COL, TRIPLE_TOP_COL,
                       TRIPLE_START_OPEN_COL, TRIPLE_START_HIGH_COL, TRIPLE_START_LOW_COL, TRIPLE_START_CLOSE_COL, TRIPLE_START_VOLUME_COL,
                       TRIPLE_END_OPEN_COL, TRIPLE_END_HIGH_COL, TRIPLE_END_LOW_COL, TRIPLE_END_CLOSE_COL, TRIPLE_END_VOLUME_COL,
                       I_BB_BBH, I_BB_BBL, I_KCH_HIGH, I_KCH_LOW, I_SQUEEZE, I_RSI,
                       I_ROC, I_TSI, I_MFI, I_VWAP, I_ATR, I_ADX, I_OBV, I_POCKET_PIVOT, I_CMF,
                       I_AROON_UP, I_AROON, I_AROON_DOWN, I_SMA,
                       I_EMA20, I_EMA50, I_MACD_DIFF
                       ]


# calc rewards
REWARDS_REWARD_COL = "reward"

# number in range (0,1), indicating multiplier for future rewards
REWARD_LAMBDA = _ucnf.REWARD_LAMBDA
# number of renkos to check in future for each matrix
REWARD_WINDOW = _ucnf.REWARD_WINDOW

REWARDS_FILE = "rewards.csv"
REWARDS_COLUMNS = [RENKO_START_DATE_COL, RENKO_START_UNIX_COL, RENKO_END_DATE_COL, RENKO_END_UNIX_COL, REWARDS_REWARD_COL]

# calc matrices

# this number indicates number of matrix rows
MATRIX_ROWS_SIZE = _ucnf.MATRIX_ROWS_SIZE
# number in range (0,1), indicating how much we want to lower renko brick size, where 1 means we dont want to lower it
ATR_NUMERIC = _ucnf.ATR_NUMERIC  # 0.25 # BTC # 0.5 # GOOGL

# matrix is X
X_TRAINING_FILE = "training_x.npy"
X_TESTING_FILE = "testing_x.npy"
X_COLUMNS = [I_BB_BBH, I_BB_BBL, I_KCH_HIGH, I_KCH_LOW, I_SQUEEZE, I_RSI,
             I_ROC, I_TSI, I_MFI, I_VWAP, I_ATR, I_ADX, I_OBV, I_POCKET_PIVOT, I_CMF,
             I_AROON_UP, I_AROON, I_AROON_DOWN, I_SMA,
             I_EMA20, I_EMA50,  # I_EMA100, I_EMA200,
             I_MACD_DIFF, RENKO_DIRECTION_COL]

# rewards is Y
Y_TRAINING_FILE = "training_y.npy"
Y_TESTING_FILE = "testing_y.npy"
Y_COLUMNS = [REWARDS_REWARD_COL]

# metadata contains all cols from triples == triples.csv
METADATA_TRAINING_FILE = "training_metadata.npy"
METADATA_TESTING_FILE = "testing_metadata.npy"
METADATA_COLUMNS = [
    TRIPLE_START_UNIX_COL, TRIPLE_END_UNIX_COL, TRIPLE_DIRECTION_COL,
    TRIPLE_BOTTOM_COL, TRIPLE_TOP_COL,
    TRIPLE_START_OPEN_COL, TRIPLE_START_HIGH_COL, TRIPLE_START_LOW_COL, TRIPLE_START_CLOSE_COL, TRIPLE_START_VOLUME_COL,
    TRIPLE_END_OPEN_COL, TRIPLE_END_HIGH_COL, TRIPLE_END_LOW_COL, TRIPLE_END_CLOSE_COL, TRIPLE_END_VOLUME_COL,
    I_BB_BBH, I_BB_BBL, I_KCH_HIGH, I_KCH_LOW, I_SQUEEZE, I_RSI,
    I_ROC, I_TSI, I_MFI, I_VWAP, I_ATR, I_ADX, I_OBV, I_POCKET_PIVOT, I_CMF,
    I_AROON_UP, I_AROON, I_AROON_DOWN, I_SMA,
    I_EMA20, I_EMA50,  # I_EMA100, I_EMA200,
    I_MACD_DIFF
]

# TRAINING CONFIGURATION

# THRESHOLDS
#    'rsi': 50,
#    'roc': 0,
#    'tsi': 0,
#    'mfi': 50,
#    'vwap': None,  # No clear neutral threshold
#    'atr': None,  # No clear neutral threshold
#    'adx': 50,
#    'obv': None,  # No clear neutral threshold
#    'cmf': 0,
#    'macd': 0

REWARD_LIMIT = 0.3
RANDOM_REWARD_LIMIT = 0.005

MODEL_INITIALIZER_MEAN = 0.
MODEL_INITIALIZER_STDEV = 0.1

LAYER_1_FILTERS = 32
LAYER_1_KERNEL_SIZE = (2,2)
LAYER_1_ACTIVATION = 'relu'
LAYER_1_INPUT_SHAPE = (MATRIX_ROWS_SIZE, len(X_COLUMNS), 1)

LAYER_2_FILTERS = 64
LAYER_2_KERNEL_SIZE = (3,3)
LAYER_2_ACTIVATION = 'relu'

LAYER_3_FILTERS = 128
LAYER_3_KERNEL_SIZE = (3,3)
LAYER_3_ACTIVATION = 'relu'

LAYER_4_DROP_OUT_RATE = 0.35

# LAYER 5 Flatten

LAYER_6_DENSE_UNITS = 128

LAYER_7_DROP_OUT_RATE = 0.25

LAYER_8_DENSE_UNITS = 1

ADAM_LEARNING_RATE = 0.001

MODEL_METRICS =['mse']

# number of epochs for training, indicating how many times algorithm goes through entire dataset to learn
EPOCHS = _ucnf.EPOCHS  # 150 # BTC # 130 # GOOGL ... 150*8 with batch 256
BATCH_SIZE = _ucnf.BATCH_SIZE  # default 32

# prediction results
PREDICTION_FILE_NAME = "predictions.npy"

# backtesting files and parameters

BACKTEST_LOG_NONE = "NONE"
BACKTEST_LOG_BASIC = "BASIC"
BACKTEST_LOG_FULL = "FULL"
BACKTEST_LOG_BOTH = "BOTH"

BACKTEST_PREDICTION_FILE_NAME = "matrix_predictions.csv"
BACKTEST_CANDLE_PREDICTIONS_FILE_NAME = "candle_predictions.csv"

BACKTEST_MODELS_BY_STOCKS = _ucnf.BACKTEST_MODELS_BY_STOCKS
BACKTEST_ONLY_CREATE_ADVICES = _ucnf.BACKTEST_ONLY_CREATE_ADVICES
BACKTEST_MODELS_LIST = _ucnf.BACKTEST_MODELS_LIST
BACKTEST_STOCK_LIST = _ucnf.BACKTEST_STOCK_LIST

BACKTEST_USING_TFT = _ucnf.BACKTEST_USING_TFT


# BACKTESTING TFT


# params
TFT_BATCH_SIZE = 64
TFT_NUM_WORKERS = 12
TFT_VAL_LENGTH = 2000
TFT_TRIPLES_COUNT_FOR_INPUT = 2000

# params
TFT_MIN_PREDICTION_LENGTH = 1  # 13 # 13 * 3
TFT_MAX_PREDICTION_LENGTH = 1  # 13 # 13 * 3
TFT_MAX_ENCODER_LENGTH = 50  # 13 * 20

TFT_TARGET = TRIPLE_DIRECTION_COL
TFT_COVARIATES_TRIPLES = ['direction', 'bb_bbh', 'bb_bbl', 'kch_high', 'kch_low', 'squeeze', 'rsi', 'roc',
                          'tsi', 'mfi', 'vwap', 'atr', 'adx', 'obv',
                          'pocket_pivot', 'cmf', 'aroon_up', 'aroon', 'aroon_down', 'sma',
                          'ema20', 'ema50', 'macd_diff']


# simulation files and parameters

OPERATION_BUY = "BUY"
OPERATION_SELL = "SELL"
OPERATION_NONE = "NONE"

ACTION_LONG = "LONG"
ACTION_SHORT = "SHORT"
ACTION_CLOSE = "CLOSE"
ACTION_COVER = "COVER"

ADVICE_TYPE_UNKNOWN = -10
ADVICE_BUY = 1
ADVICE_SELL = -1
ADVICE_NEUTRAL = 0

CNN_PREDICTION_BUY_LIMIT = _ucnf.CNN_PREDICTION_BUY_LIMIT  # default = 0.0, before 0.0
CNN_PREDICTION_BUY_LIMIT_MAX = _ucnf.CNN_PREDICTION_BUY_LIMIT_MAX  # default = 0.0, before 4.5

TFT_PREDICTION_BUY_LIMIT = _ucnf.TFT_PREDICTION_BUY_LIMIT  # default = 0.0, before 0.0
TFT_PREDICTION_BUY_LIMIT_MAX = _ucnf.TFT_PREDICTION_BUY_LIMIT_MAX  # default = 0.0, before 4.5

SIMULATION_INIT_BALANCE = 10000.0
SIMULATION_DECIMAL_PRECISION = 6

SIMULATION_CURRENT_PRICE_ACTUAL_CLOSE = "ACTUAL_CLOSE"
SIMULATION_CURRENT_PRICE_NEXT_OPEN = "NEXT_OPEN"
SIMULATION_CURRENT_PRICE_TYPE = _ucnf.SIMULATION_CURRENT_PRICE_TYPE

ACTION_END_NORMAL = 0
ACTION_END_STOPLOSS = 1
ACTION_END_OVERNIGHT = 2

# actions csv
ACTION_COL = "action"
OPERATION_COL = "operation"
OPERATION_PRICE_COL = "operation_price"
OPERATION_STOP_PRICE_COL = "operation_stop_price"
PRICE_COL = "price"
OPERATION_END_TYPE = "operation_end_type"

ACTIONS_FILE = "actions.csv"
ACTION_COLUMNS = [UNIX_COL, DATE_COL, ACTION_COL, OPERATION_COL, OPERATION_PRICE_COL, OPERATION_STOP_PRICE_COL,
                  PRICE_COL, OPEN_COL, HIGH_COL, LOW_COL, CLOSE_COL, OPERATION_END_TYPE]

# trades csv
TRADE_COL = "trade"

TRADES_FILE = "trades.csv"
TRADES_COLUMNS = [UNIX_COL, DATE_COL, TRADE_COL, PRICE_COL, OPEN_COL, HIGH_COL, LOW_COL, CLOSE_COL]

# advice csv
PREDICTION_COL = "prediction"
ADVICE_COL = "advice"

ADVICE_FILE = "advices.csv"
ADVICE_COLUMNS = [UNIX_COL, DATE_COL, ADVICE_COL, PRICE_COL, OPEN_COL, HIGH_COL, LOW_COL, CLOSE_COL]

# balance csv columns
BALANCE_TOTAL_QUOTE_COL = "total_quote"  # base + quote
BALANCE_BASE_COL = "base"
BALANCE_QUOTE_COL = "quote"
BALANCE_DEBT_BASE_COL = "debt_base"
BALANCE_GAIN = "gain"
PRICE_GAIN_COL = "price_gain"
DAY_COL = "day"

BALANCE_FILE = "balance.csv"
BALANCE_PLOT_FILE_NAME = "gain.png"


# ========

STOP_LOSS_LEVEL = _ucnf.STOP_LOSS_LEVEL


# Martin's emulate code
PLOT_EMULATE_EXPORT_FOLDER_PATH = EXPERIMENT_DATA_PATH + 'emulate/data/'
PLOT_EMULATE_FILE_NAME = "plt.png"
PLOT_EMULATE_STATS_FILE_NAME = 'stats.csv'
EMULATE_MAX_ALLOWED_LOSS = -STOP_LOSS_LEVEL*100  # stop loss value # unused
EMULATE_TICKER = 'GOOGL'  # unused
EMULATE_START_CAPITAL = 10000.0  # const  # unused
#
#
# TRADE_FILE_NAME = "trades.csv"
# CANDLE_OPERATIONS_FILE_NAME = "candle_operations.csv"
# ACTION_FILE_NAME = "actions.csv"
# STATE_FILE_NAME = "states.csv"
# OPERATIONS_FILE_NAME = "operations.csv"
# OPERATIONS_FULL_FILE_NAME = "operations_full.csv"
# BALANCE_FILE_NAME = "balance.csv"
# BALANCE_PLOT_FILE_NAME = "balance.png"
# PLOT_SIMULATE_EXPORT_FOLDER_PATH = EXPERIMENT_DATA_PATH + 'step4_simulate/plot/'
# DATA_SIMULATE_EXPORT_FOLDER_PATH = EXPERIMENT_DATA_PATH + 'step4_simulate/data/'
#
#
# STATE_COL = "state"
# STATE_STOP_ACTIVATED_COL = "stop_activated"
# STATE_LIMIT_ACTIVATED_COL = "limit_activated"
#
# STATE_NEUTRAL = "NEUTRAL"
# STATE_LONG = "LONG"
# STATE_SHORT = "SHORT"
# STATE_CLOSE = "CLOSE"
# STATE_COVER = "COVER"
# STATE_HOLD_LONG = "HOLD_L"
# STATE_HOLD_SHORT = "HOLD_S"
# STATE_DEFAULT_VALUE = STATE_NEUTRAL
#
# ACTION_COL = "action"
# STOP_PRICE_COL = "stop_price"
# PRICE_COL = "price"
#
# ACTION_NEUTRAL = "NEUTRAL"
# ACTION_LONG = "LONG"
# ACTION_SHORT = "SHORT"
# ACTION_CLOSE = "CLOSE"
# ACTION_COVER = "COVER"
# ACTION_HOLD_LONG = "HOLD_L"
# ACTION_HOLD_SHORT = "HOLD_S"
# ACTION_WAITING_FOR_LIMIT_AFTER_STOP_LOSS = "WAITING_FOR_LIMIT_AFTER_STOP_LOSS"
# ACTION_NEUTRAL_AFTER_STOP_LOSS_LONG = "NEUTRAL_AFTER_STOP_LOSS_LONG"
# ACTION_NEUTRAL_AFTER_STOP_LOSS_SHORT = "NEUTRAL_AFTER_STOP_LOSS_SHORT"
# ACTION_NEUTRAL_AFTER_STOP_LOSS_NEUTRAL_SHOULD_NOT_APPEAR = "NEUTRAL_AFTER_STOP_LOSS_NEUTRAL_SHOULD_NOT_APPEAR"
# ACTION_DEFAULT_VALUE = STATE_NEUTRAL
#
# OPERATION_COL = "operation"
# OPERATION_PRICE_COL = "operation_price"
# OPERATION_BUY = "BUY"
# OPERATION_SELL = "SELL"
# OPERATION_NONE = "NONE"
# OPERATION_NONE_ZERO_BALANCE_BUY = "NONE_ZB_BUY"  # it should be buy, but it is none because of zero balance
# OPERATION_NONE_ZERO_BALANCE_SELL = "NONE_ZB_SELL"  # it should be sell, but it is none because of zero balance
# # in real world trading, API require for trade a minimum amount for trade, use below parameters
# ZERO_BALANCE_BASE = 0.0  # at which balance we represent base balance as zero balance, and not doing buy/sell.
# ZERO_BALANCE_QUOTE = 0.0  # at which balance we represent quote balance as zero balance, and not doing buy/sell.
#
# OPERATION_ACTION_SOURCE_COL = "operation_action_source"
#
# OPERATION_ACTION_SOURCE_LONG = "LONG"
# OPERATION_ACTION_SOURCE_CLOSE = "CLOSE"
# OPERATION_ACTION_SOURCE_CLOSE_STOP = "CLOSE_STOP"
# OPERATION_ACTION_SOURCE_SHORT = "SHORT"
# OPERATION_ACTION_SOURCE_COVER = "COVER"
# OPERATION_ACTION_SOURCE_COVER_STOP = "COVER_STOP"
# OPERATION_ACTION_SOURCE_NONE = "NONE"
#
# SIMULATION_INIT_BALANCE = _ucnf.SIMULATION_INIT_BALANCE
# SIMULATION_DECIMAL_PRECISION = _ucnf.SIMULATION_DECIMAL_PRECISION
#
# BACKTEST_LOG_NONE = "NONE"
# BACKTEST_LOG_BASIC = "BASIC"
# BACKTEST_LOG_FULL = "FULL"
# BACKTEST_LOG_BOTH = "BOTH"
#
# BALANCE_TOTAL_QUOTE_COL = "total_quote"  # base + quote
# BALANCE_BASE_COL = "base"
# BALANCE_QUOTE_COL = "quote"
# BALANCE_DEBT_BASE_COL = "debt_base"
# BALANCE_GAIN = "gain"
# PRICE_GAIN_COL = "price_gain"
#
# DAY_COL = "day"  # it is datetime format from unix : datetime.datetime.fromtimestamp(int(x))
#
# BACKTEST_DATA_DIRECTORY_PATH = EXPERIMENT_DATA_PATH + "step5_backtest/data/"
#
# BACKTEST_RESULT_FILE_NAME = "matrix_predictions.csv"
# BACKTEST_CANDLE_PREDICTIONS_FILE_NAME = "candle_predictions.csv"
# BACKTEST_TRADE_FILE_NAME = "trades.csv"

PREDICTION_RESULT_FORMAT = '%.'+str(int(SIMULATION_DECIMAL_PRECISION))+'f'

_full_config = locals()


def INPUT_OHLCV_FILE_PATH(stock_name):
    return BASE_STOCK_TXT_FILES_PATH + stock_name + ".txt"


def METADATA_DIRECTORY_PATH():
    return BASE_METADATA_FILES_PATH

def LOADED_DATA_PATH(stock_name):
    return METADATA_DIRECTORY_PATH() + stock_name+ "/"


def MATRICES_DIRECTORY_PATH():
    return BASE_MATRICES_FILES_PATH

def TRAINING_DATA_PATH(stock_name):
    return MATRICES_DIRECTORY_PATH() + stock_name + "/"

def X_TRAINING_FILE_PATH(stock_name):
    return TRAINING_DATA_PATH(stock_name) + X_TRAINING_FILE


def X_TESTING_FILE_PATH(stock_name):
    return TRAINING_DATA_PATH(stock_name) + X_TESTING_FILE


def Y_TRAINING_FILE_PATH(stock_name):
    return TRAINING_DATA_PATH(stock_name) + Y_TRAINING_FILE


def Y_TESTING_FILE_PATH(stock_name):
    return TRAINING_DATA_PATH(stock_name) + Y_TESTING_FILE


def METADATA_TRAINING_FILE_PATH(stock_name):
    return TRAINING_DATA_PATH(stock_name) + METADATA_TRAINING_FILE


def METADATA_TESTING_FILE_PATH(stock_name):
    return TRAINING_DATA_PATH(stock_name) + METADATA_TESTING_FILE


def MODELS_DIRECTORY_PATH():
    return BASE_MODELS_FILES_PATH

def PREDICTION_DIRECTORY_PATH():
    return BASE_PREDICTIONS_FILES_PATH

def PREDICTION_FILE_PATH(model_name):
    return PREDICTION_DIRECTORY_PATH()+model_name+ "_"+PREDICTION_FILE_NAME

def BACKTEST_DIRECTORY_PATH():
    return BASE_BACKTEST_DATA_DIRECTORY_PATH

def BACKTEST_DATA_MODEL_STOCK_PATH(model, stock_name):
    return BACKTEST_DIRECTORY_PATH() + model + "/" + stock_name + "/"

def BACKTEST_STOCK_TRIPLES_PATH(stock_name):
    return BACKTEST_DIRECTORY_PATH() + stock_name + "/"

def SIMULATION_INPUT_ACTIONS_DIRECTORY_PATH():
    return BASE_SIMULATION_INPUT_ACTION_FILES_PATH


def SIMULATION_INPUT_TRADES_DIRECTORY_PATH():
    return BASE_SIMULATION_INPUT_TRADES_FILES_PATH

def SIMULATION_INPUT_ADVICES_DIRECTORY_PATH():
    return BASE_SIMULATION_INPUT_ADVICES_FILES_PATH


def SIMULATION_METADATA_DIRECTORY_PATH(stock_name):
    return BASE_SIMULATION_METADATA_FILES_PATH+"/"+stock_name+"/"


def SIMULATION_METADATA_OHLCV_FILE_PATH(stock_name):
    return SIMULATION_METADATA_DIRECTORY_PATH(stock_name)+OHLCV_FILE


def SIMULATION_METADATA_ACTION_DIRECTORY_PATH(stock_name, strategy, as_folder=False):
    if as_folder:
        return SIMULATION_METADATA_DIRECTORY_PATH(stock_name) + strategy + "/"
    return SIMULATION_METADATA_DIRECTORY_PATH(stock_name)+"/"+strategy+"/"+ACTIONS_FILE


def SIMULATION_METADATA_TRADES_DIRECTORY_PATH(stock_name, strategy, as_folder=False):
    if as_folder:
        return SIMULATION_METADATA_DIRECTORY_PATH(stock_name) + strategy + "/"
    return SIMULATION_METADATA_DIRECTORY_PATH(stock_name)+strategy+"/"+TRADES_FILE


def SIMULATION_METADATA_ADVICES_DIRECTORY_PATH(stock_name, strategy, as_folder=False):
    if as_folder:
        return SIMULATION_METADATA_DIRECTORY_PATH(stock_name) + strategy + "/"
    return SIMULATION_METADATA_DIRECTORY_PATH(stock_name)+strategy+"/"+ADVICE_FILE


def SIMULATION_BALANCE_DIRECTORY_PATH():
    return BASE_SIMULATION_BALANCE_DIRECTORY_PATH


def balance_data_directory_path():
    return SIMULATION_BALANCE_DIRECTORY_PATH() + SIMULATION_BALANCE_DATA_DIRECTORY_NAME


def get_stock_action_name(action_file):
    name_parts = action_file.split("_", 1)
    assert len(name_parts) == 2, "action name must be in format [STOCK_NAME]_[ACTION_NAME] : found "+action_file
    return name_parts[0], "_".join(name_parts[1:])


def get_stock_trade_name(trade_file):
    name_parts = trade_file.split("_", 1)
    assert len(name_parts) == 2, "trade name must be in format [STOCK_NAME]_[TRADE_NAME] : found "+trade_file
    return name_parts[0], "_".join(name_parts[1:])


def get_stock_advice_name(advice_file):
    name_parts = advice_file.split("_", 1)
    assert len(name_parts) == 2, "advice name must be in format [STOCK_NAME]_[ADVICE_NAME] : found "+advice_file
    return name_parts[0], "_".join(name_parts[1:])


def get_advice_file_path(stock_name, model_name):
    return SIMULATION_INPUT_ADVICES_DIRECTORY_PATH()+stock_name+"_"+model_name+".csv"

def save_config_file():
    if not _os.path.exists(EXPERIMENT_DATA_PATH+"log/"):
        _os.makedirs(EXPERIMENT_DATA_PATH+"log/")
    file1 = open(_os.path.abspath(__file__), "r")
    file2 = open(EXPERIMENT_DATA_PATH + "log/parameter_config.py", "w")
    file2.write(file1.read())
    file1.close()
    file2.close()
    # _os.system("cp "+ _os.path.abspath(__file__) + " " + EXPERIMENT_DATA_PATH + "log/parameter_config.py")

    values = {}
    for name in [item for item in _full_config if not item.startswith("_")]:
        value = eval(name)
        if not callable(value):
            values[name] = eval(name)
    with open(EXPERIMENT_DATA_PATH+"log/"+FULL_CONFIG_FILE, "w") as outfile:
        outfile.write(_json.dumps(values, indent=4))

    values = {}
    for name in [item for item in _ucnf._config_variables if not item.startswith("_")]:
        value = eval("_ucnf."+name)
        if not callable(value):
            values[name] = value
    with open(EXPERIMENT_DATA_PATH+"log/"+USER_CONFIG_FILE, "w") as outfile:
        outfile.write(_json.dumps(values, indent=4))