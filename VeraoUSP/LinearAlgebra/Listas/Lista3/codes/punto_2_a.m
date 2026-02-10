pkg load symbolic

syms lambda
T_1 = [1, 0, 1; 0, 2, 3; -1, 0, -4];
char_poly = det(T_1 - lambda * eye(3));
char_poly_expanded = factor(char_poly);
disp('Characteristic polynomial:');
latex(char_poly_expanded);
