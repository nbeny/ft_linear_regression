from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

# classifier example
from sklearn.svm import SVC

pipeline = make_pipeline(Normalizer(), SVC())
