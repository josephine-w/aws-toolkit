import json
import boto3

folders = []
folder_map = dict()
with open('output.manifest', 'r') as manifest:
    data = manifest.read().split('\n')
    for d in data:
        if d != "":
            input = json.loads(d)
            image_url = input['source-ref']

            x = image_url.rindex('_')
            y = image_url.rindex('/')
            image_folder = image_url.replace(image_url[:x + 1], '').replace('.jpeg', '')
            image_file = image_url.replace(image_url[:y + 1], '').replace('.jpeg', '')
            image_folder += '/'

            if image_folder not in folder_map:
                folder_map[image_folder] = []

            folder_map[image_folder].append(image_file)
            folders.append(image_folder)

s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
input_bucket = 'inputbucket123'  # change to input bucket
output_bucket = 'outputbucket123'  # change to output bucket

bucket = s3.Bucket(input_bucket)

# print(len(folder_map))

for f in folders:
    for obj in bucket.objects.filter(Prefix=f):
        if (folder_map[f] in obj.key) and (('.jpg' in obj.key) or ('.jpeg' in obj.key)):
            input_key = obj.key
            z = obj.key.rindex('/')
            output_key = obj.key.replace(obj.key[:z + 1], '')

    # print('FILE NO.: {}, INPUT KEY: {}, OUTPUT KEY: {}'.format(counter, input_key, output_key))

    source = {
        'Bucket': input_bucket,
        'Key': input_key
    }

    s3.meta.client.copy(source, output_bucket, '2020-10-06/' + output_key)
