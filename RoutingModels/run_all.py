"""Run every Section 3.9 model in order and print the output.

    python run_all.py              # prints to the screen
    python run_all.py > output.txt # to compare against expected_output.txt
"""
import jurisdiction_inference, skew_gap, closed_form, coincidence_exact

print("== jurisdiction_inference.py ==")
jurisdiction_inference.main()
print("\n== skew_gap.py ==")
skew_gap.main()
print("\n== closed_form.py ==")
closed_form.main()
print("\n== coincidence_exact.py ==")
coincidence_exact.main()
