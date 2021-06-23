import os
import argparse

subprocess.run(["curl https://push.databox.com", "-u <your_token>:", "-X POST", "-H 'Content-Type: application/json'","-H 'Accept: application/vnd.databox.v2+json'", "-d '{
  "data":[
    {
      "$sales": 420,
      "$visitors": 123000
    }
  ]
}'"])
