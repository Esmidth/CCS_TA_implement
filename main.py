from absl import app
from absl import flags
from absl import logging
import utils

flags.DEFINE_string(
    'hello_world','helloworld','flags test string'
)

FLAGS = flags.FLAGS

def main(argv):
    del argv
    # print(FLAGS.hello_world)

    df = utils.get_data('rat')
    print(df.columns)


if __name__ == '__main__':
    app.run(main)