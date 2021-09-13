# Python Flask application to Google Cloud Run using Cloud Build

Taken from https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python

Google Cloud Run is for Serverless Applications

### How to deploy
1. Deploy from source using the following command:

`gcloud run deploy`

If prompted to enable the API, Reply y to enable.

When you are prompted for the source code location, press Enter to deploy the current folder.

When you are prompted for the service name, press Enter to accept the default name, helloworld.

If you are prompted to enable the Artifact Registry API, respond by pressing 'y'.

When you are prompted for region: select the region of your choice, for example us-central1.

You will be prompted to allow unauthenticated invocations: respond y .

Then wait a few moments until the deployment is complete. On success, the command line displays the service URL.

2. Visit your deployed service by opening the service URL in a web browser.