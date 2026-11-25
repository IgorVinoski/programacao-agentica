import Mathlib

theorem limpo_soma (n : ℕ) : 2 * (Finset.range (n + 1)).sum id = n * (n + 1) := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    simp [id]
    ring
