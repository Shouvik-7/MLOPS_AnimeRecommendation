from utils.helpers import *
from config.paths_config import *
from pipeline.prediction_pipeline import hybrid_recommendation 

#print(find_similar_animes('Fairy Tail', ANIME_WEIGHTS_PATH, ANIME2ANIME_ENCODED, ANIME2ANIME_DECODED, DF))

print(hybrid_recommendation(11880))