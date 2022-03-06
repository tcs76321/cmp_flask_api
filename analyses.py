from flask import Flask, request, jsonify


def singleAnalysis(metabolite, level):
    if str(metabolite) == "albumin":
        result = 35 < level < 55
    elif str(metabolite) == "bun":
        result = 80 < level < 200
    elif str(metabolite) == "calcium":
        result = 86 < level < 102
    elif str(metabolite) == "co2":
        result = 23 < level < 28
    elif str(metabolite) == "chloride":
        result = 98 < level < 106
    elif str(metabolite) == "creatine":
        result = 5 < level < 13
    elif str(metabolite) == "glucose":
        result = 700 < level < 990
    elif str(metabolite) == "potassium":
        result = 35 < level < 50
    elif str(metabolite) == "sodium":
        result = 136 < level < 145
    elif str(metabolite) == "total-bilirubin":
        result = 3 < level < 10
    elif str(metabolite) == "total-protein":
        result = 55 < level < 90
    elif str(metabolite) == "alt":
        result = 10 < level < 40
    elif str(metabolite) == "alp":
        result = 30 < level < 120
    elif str(metabolite) == "ast":
        result = 10 < level < 40
    else:
        response = f"Sorry, we do not currently support {metabolite} as a metabolite, yet"
        return response

    if result:
        result = "IN reference range"
    else:
        result = "OUT reference range"

    response = jsonify(metabolite, level, result)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def fullAnalysis():
    response = jsonify("in development")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
