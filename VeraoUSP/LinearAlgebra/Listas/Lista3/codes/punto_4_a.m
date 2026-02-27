A = [-9, 4, 4; -8, 3, 4; -16, 8, 7];

disp("Original Matrix");
disp(A);

[P, D] = eig(A);

disp("Matrix P (Eigenvectors):");
disp(P);
disp("Matrix D (Diagonal Eigenvalues):");
disp(D);

A_reconstructed = P * D * inv(P);
disp("Reconstructed A (P * D * inv(P)):");
disp(A_reconstructed);

if (max(max(abs(A - A_reconstructed))) < 1e-10)
    disp("Verification successful: A is diagonalizable.");
else
    disp("Verification failed or A is not diagonalizable.");
end
