class FairnessReport:

    def generate(self, reports):

        print("=" * 80)

        print("ENTERPRISE AI FAIRNESS REPORT")

        print("=" * 80)

        overall_safe = True

        for report in reports:

            print()

            print(f"Protected Attribute : {report['attribute']}")

            print(

                f"Comparison : "

                f"{report['value_a']} "

                f"vs "

                f"{report['value_b']}"

            )

            print()

            print("Decision A :", report["decision_a"])

            print("Decision B :", report["decision_b"])

            print()

            print("Response A")

            print("-" * 40)

            print(report["response_a"])

            print()

            print("Response B")

            print("-" * 40)

            print(report["response_b"])

            print()

            print("Bias Result")

            print("-" * 40)

            print(report["bias"])

            if not report["bias"].safe:

                overall_safe = False

        print()

        print("=" * 80)

        print(

            "Overall Result :",

            "PASS" if overall_safe else "FAIL",

        )

        print("=" * 80)