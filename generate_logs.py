#!/usr/bin/env python3
"""
generate_logs.py - Script de génération de logs aléatoires
Membre 2 : Ingestion de Logs (Apache Flume)
Mini-Projet Big Data - ENSA Agadir
"""

import random
import time
import datetime

# Données simulées
ACTIONS = ["LOGIN", "LOGOUT", "PURCHASE", "VIEW_PRODUCT", "ADD_TO_CART",
           "REMOVE_FROM_CART", "SEARCH", "PAYMENT", "ERROR", "TIMEOUT"]

USERS = ["user_" + str(i) for i in range(1, 51)]

SERVICES = ["auth-service", "product-service", "cart-service",
            "payment-service", "search-service", "api-gateway"]

LEVELS = ["INFO", "INFO", "INFO", "WARN", "ERROR"]  # INFO plus fréquent

PRODUCTS = ["laptop", "smartphone", "tablet", "headphones", "keyboard",
            "mouse", "monitor", "webcam", "speaker", "charger"]

IP_PREFIXES = ["192.168.1.", "10.0.0.", "172.16.0."]


def generate_ip():
    prefix = random.choice(IP_PREFIXES)
    return prefix + str(random.randint(1, 254))


def generate_log_line():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(LEVELS)
    service = random.choice(SERVICES)
    user = random.choice(USERS)
    action = random.choice(ACTIONS)
    ip = generate_ip()
    product = random.choice(PRODUCTS)
    duration_ms = random.randint(10, 5000)

    if action in ["VIEW_PRODUCT", "ADD_TO_CART", "REMOVE_FROM_CART", "PURCHASE"]:
        message = (
            f"{timestamp} [{level}] {service} - user={user} "
            f"action={action} product={product} ip={ip} duration={duration_ms}ms"
        )
    elif action == "SEARCH":
        query = random.choice(PRODUCTS)
        results = random.randint(0, 200)
        message = (
            f"{timestamp} [{level}] {service} - user={user} "
            f"action={action} query={query} results={results} ip={ip} duration={duration_ms}ms"
        )
    elif action == "PAYMENT":
        amount = round(random.uniform(5.0, 1500.0), 2)
        status = random.choice(["SUCCESS", "FAILED", "PENDING"])
        message = (
            f"{timestamp} [{level}] {service} - user={user} "
            f"action={action} amount={amount}USD status={status} ip={ip} duration={duration_ms}ms"
        )
    elif action == "ERROR":
        error_codes = ["500", "503", "404", "401", "403"]
        code = random.choice(error_codes)
        message = (
            f"{timestamp} [ERROR] {service} - user={user} "
            f"action={action} error_code={code} ip={ip} duration={duration_ms}ms"
        )
    else:
        message = (
            f"{timestamp} [{level}] {service} - user={user} "
            f"action={action} ip={ip} duration={duration_ms}ms"
        )

    return message


if __name__ == "__main__":
    # Génération continue de logs (1 log toutes les 0.5 secondes)
    while True:
        log_line = generate_log_line()
        print(log_line, flush=True)
        time.sleep(0.5)
