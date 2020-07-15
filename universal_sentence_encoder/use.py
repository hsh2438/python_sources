import tensorflow as tf
import tensorflow_hub as hub


gpu_num = 1

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_visible_devices(gpus[gpu_num], 'GPU')
        tf.config.experimental.set_memory_growth(gpus[gpu_num], True)
    except RuntimeError as e:
        print(e)
        
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
