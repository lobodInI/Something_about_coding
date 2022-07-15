from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument('name', type=str)

args = vars(args.parse_args())

print(args)