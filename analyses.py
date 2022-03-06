from flask import Flask, request, jsonify


def singleAnalysis(metabolite, level):
    if str(metabolite) == "albumin":
        result = 35 < level < 55
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "bun":
        result = 80 < level < 200
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "calcium":
        result = 86 < level < 102
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "co2":
        result = 23 < level < 28
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "chloride":
        result = 98 < level < 106
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "creatine":
        result = 5 < level < 13
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "glucose":
        result = 700 < level < 990
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "potassium":
        result = 35 < level < 50
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "sodium":
        result = 136 < level < 145
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "total-bilirubin":
        result = 3 < level < 10
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "total-protein":
        result = 55 < level < 90
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "alt":
        result = 10 < level < 40
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "alp":
        result = 30 < level < 120
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    elif str(metabolite) == "ast":
        result = 10 < level < 40
        if result:
            result = "IN reference range"
        else:
            result = "OUT reference range"
        response = jsonify(metabolite, level, result)
        return response
    else:
        response = f"Sorry, we do not currently support {metabolite} as a metabolite, yet"
        return response


def comprehensive():
    response = jsonify(albumin="within limits", bun="above recommended limit")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
