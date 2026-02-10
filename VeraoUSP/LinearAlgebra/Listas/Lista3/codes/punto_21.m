% For Simplicity I'll cut to the meat of the discussion
% Meaning I'll firstly show that it's not diagonazable in R but it is in C
A = [-2 0 -1; 0 5 0; -1 0 -2];

[P, D] = eig(A);

disp('Eigenvector matrix V:');
disp(P);

disp('Eigenvalues matrix V:');
disp(D);

disp('Rank of V:');
disp(rank(P));

eigenvalues = diag(D);
hasComplexEigenvalues = any(imag(eigenvalues) ~= 0);
if hasComplexEigenvalues
  disp("It have complex Eigenvalues, Therefore it cannot be diagonalizable in R")
 end

if rank(P) < length(A)
    disp('Matrix is nogt diagonalizable.');
end

disp("To check that it is diagonalizable see that")
A_reconstructed = P * D * inv(P);
disp("Reconstructed A (P * D * inv(P)):");
disp(A_reconstructed);

if (max(max(abs(A - A_reconstructed))) < 1e-10)
    disp("Verification successful: A is diagonalizable.");
else
    disp("Verification failed or A is not diagonalizable.");
end
