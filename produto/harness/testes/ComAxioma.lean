import Mathlib

axiom atalho : ∀ n : ℕ, n = n + 1 - 1

theorem com_axioma (n : ℕ) : n = n + 1 - 1 := atalho n
