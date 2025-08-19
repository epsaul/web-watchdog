import dns.resolver
import yaml

def check_dns(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [r.to_text() for r in answers]
    except Exception as e:
        return f"DNS check failed: {e}"

if __name__ == "__main__":
    with open("../config/targets.yaml", "r") as f:
        targets = yaml.safe_load(f)
    for site in targets["domains"]:
        result = check_dns(site)
        print(f"{site}: {result}")
