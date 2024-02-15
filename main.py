import argparse
import base64

from predict import predict_custom_trained_model_sample

parser = argparse.ArgumentParser(description="Process ai predictor.")

parser.add_argument("--project", type=str, help="Project ID", required=True)
parser.add_argument("--endpoint_id", type=str, help="Endpoint ID", required=True)
parser.add_argument("--prompt", type=str, help="prompt for prediction", required=True)

args = parser.parse_args()

predictions = predict_custom_trained_model_sample(
    args.project, args.endpoint_id, {"prompt": args.prompt}
)

with open("img.jpg", "wb") as g:
    g.write(base64.b64decode(predictions[0]))
