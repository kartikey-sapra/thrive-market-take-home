import json

from redis import Redis

PREFIX = "prod_id_"


def get_key(k):
    return PREFIX + str(k)


def process_data(data):
    """
    Process data zip the recommended product id and their score in a dictionary
    :param data: Dict - Containing Productid, recommendations, scores
    :return: tuple of Productid and recommendation_dict
    """
    productid = data["productid"]
    recommendations = data["recommendations"]
    scores = data["scores"]

    recommendation_dict = {}
    for reco_prod, reco_score in zip(recommendations, scores):
        recommendation_dict[reco_prod] = reco_score
    return productid, recommendation_dict


def load_data_from_file(file_name, redis_instance):
    """
    Read data from the json file and load it in redis as Hashset
    :param file_name: File to read the raw data from
    :param redis_instance: Redis connection
    """
    with open(file_name, "r") as file_obj:
        for line in file_obj:
            json_line = json.loads(line)
            product_id, recommendation_dict = process_data(json_line)
            key = get_key(product_id)
            redis_instance.hmset(key, recommendation_dict)


if __name__ == "__main__":
    redis_inst = Redis()
    load_data_from_file("data/substitution_1-0-0_20191007.jsonl", redis_inst)
