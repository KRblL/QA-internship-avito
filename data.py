SELLER_ID = 117177
SELLER_ID2 = 117178
INVALID_SELLER_ID = [0, -1, 3.14, "qwerty"]

GET_INVALID_ID = "777"
GET_NON_EXISTENT_ID = "9c18fc22-0575-4012-98e8-8bdccb677777"


CREATE_VALID_PAYLOAD = {
    "sellerID": 117177,
    "name": "krbll",
    "price": 50001,
    "statistics": {
        "likes": 13,
        "viewCount": 27,
        "contacts": 43
    }
}

CREATE_VALID_PAYLOAD2 = {
    "sellerID": 117178,
    "name": "krbll",
    "price": 50001,
    "statistics": {
        "likes": 13,
        "viewCount": 27,
        "contacts": 43
    }
}

# Отсутствует sellerID
CREATE_PAYLOAD_WITHOUT_SELLERID = {
    "name": "krbll",
    "price": 50001,
    "statistics": {
        "likes": 13,
        "viewCount": 27,
        "contacts": 43,
    },
}

# Отсутствует name
CREATE_PAYLOAD_WITHOUT_NAME = {
    "sellerID": 117177,
    "price": 50001,
    "statistics": {
        "likes": 13,
        "viewCount": 27,
        "contacts": 43,
    },
}

# Отсутствует price
CREATE_PAYLOAD_WITHOUT_PRICE = {
    "sellerID": 117177,
    "name": "krbll",
    "statistics": {
        "likes": 13,
        "viewCount": 27,
        "contacts": 43,
    },
}

# Отсутствует statistics
CREATE_PAYLOAD_WITHOUT_STATISTICS = {
    "sellerID": 117177,
    "name": "krbll",
    "price": 50001,
}

CREATE_PAYLOAD_INVALID_SELLERID = [
    {
        "sellerID": 0,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": "",
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 3.14,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": "qwerty",
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": -777,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    }
]

CREATE_PAYLOAD_INVALID_NAME = [
    {
        "sellerID": 117177,
        "name": "",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": 1234,
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "##@@  %%",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "       ",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": {},
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    }
]

CREATE_PAYLOAD_INVALID_PRICE = [
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": "",
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": "5000",
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": -50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": 43
        }
    }
]

CREATE_PAYLOAD_INVALID_STATISTICS = [
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {}
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": -13,
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": -27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": -43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": "",
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": "",
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": ""
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": "13",
            "viewCount": 27,
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": "27",
            "contacts": 43
        }
    },
    {
        "sellerID": 117177,
        "name": "krbll",
        "price": 50001,
        "statistics": {
            "likes": 13,
            "viewCount": 27,
            "contacts": "43"
        }
    }
]

CREATE_PAYLOAD_ZERO_STATISTICS = {
    "sellerID": 117177,
    "name": "krbll",
    "price": 50001,
    "statistics": {
        "likes": 0,
        "viewCount": 0,
        "contacts": 0
    }
}

CREATE_INVALID_PAYLOAD = {
    "sellerID": 117177,
    "name": "krbll",
    "price": 50001,
    "statistics": {
        "likes": 13,
        "viewCount": 27,
        "contacts": 43
    },
    "padding": "padding"
}
