import tensorflow as tf
import tensorflow_hub as hub

class UniversalSentenceEncoder:
    
    def __init__(self, model_dir):
        self.model = hub.load(model_dir)

    def get_vector(self, sentence):
        embedding = self.model([sentence])
        return embedding.numpy().tolist()[0]


if __name__ == '__main__':
    use = UniversalSentenceEncoder('../model')
    vector1 = use.get_vector('we can go ahead and set you up for service.')
    vector2 = use.get_vector('we can go ahead and set you up for service.')

    import numpy as np
    print(np.dot(vector1, vector2))
