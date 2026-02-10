Require Import List Arith.
Import ListNotations.

Fixpoint getPowersHelper (n x : nat) : list nat :=
  match n with
    | O => [1]
    | S p => if Nat.leb (Nat.pow 2 n) x
             then (Nat.pow 2 n) :: (getPowersHelper p x)
             else (getPowersHelper p x)
  end.

Definition getPowers (x : nat) : list nat :=
  getPowersHelper x x.

Example getPowersTest1 : getPowers 5 = [4; 2; 1].
Proof. reflexivity. Qed.

Definition SumTotal (x : list nat) : nat :=
  fold_right (Nat.add) 0 x.

Theorem power_greater_than_nat : forall (n : nat), SumTotal (getPowers n) >= n.
Proof.
  intros n.
  induction n.
  * simpl. lia.
