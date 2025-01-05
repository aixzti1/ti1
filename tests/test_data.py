import pandas as pd
from src.data.data_preprocessor import DataPreprocessor
from src.data.feature_engineering import FeatureEngineering

def test_preprocessor():
    df = pd.DataFrame({'close': [1,2,3]})
    processor = DataPreprocessor(df)
    processed = processor.process()
    assert not processed.empty

def test_feature_engineering():
    df = pd.DataFrame({'close': [1,2,3,4,5,6,7,8,9,10]})
    fe = FeatureEngineering(df)
    features = fe.create_features()
    assert 'ma_10' in features.columns
