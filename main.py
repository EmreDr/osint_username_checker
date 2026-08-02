from variant_generator import generate_variants
from checker import check_all_platforms
from logger import save_results


def run_once(full_name: str) -> None:
    variants = generate_variants(full_name)
    results = check_all_platforms(variants)
    save_results(full_name, results)

    for r in results:
        status = "Found" if r["found"] else "Not Found"
        print(f"  {r['platform']:10s} {r['variant']:20s} -> {status} ({r['state']})")


def main() -> None:
    print("Name finder/ q for out")
    while True:
        full_name = input("\nEnter name: ").strip()

        if full_name.lower() == "q":
            break
        if not full_name:
            print("You must enter a name.")
            continue

        run_once(full_name)


if __name__ == "__main__":
    main()