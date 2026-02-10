% ============================================
% PRODUCTO INTERNO PARA MATRICES 2x2
% (A, B) = tr(B^T * A) = sum(sum(A .* B))
% ============================================

% Función para calcular el producto interno
function producto = producto_interno(A, B)
    % Calcula tr(B^T * A) = sum_{i,j} a_ij * b_ij
    producto = sum(sum(A .* B));
end

% Función para calcular la norma de una matriz
function norma = norma_matriz(A)
    norma = sqrt(producto_interno(A, A));
end

% ============================================
% PROCESO DE GRAM-SCHMIDT PARA MATRICES 2x2
% ============================================

function base_ortonormal = gram_schmidt_matrices(base)
    % base: cell array con matrices de la base original
    % base_ortonormal: cell array con matrices ortonormalizadas

    k = length(base); % Número de matrices en la base

    % Inicializar base ortonormal
    base_ortonormal = cell(1, k);

    for i = 1:k
        % Tomar la i-ésima matriz de la base original
        v = base{i};

        % Restar proyecciones sobre las direcciones ya procesadas
        for j = 1:i-1
            % Calcular coeficiente de proyección: (v, u_j) / (u_j, u_j)
            u_j = base_ortonormal{j};
            proy_coef = producto_interno(v, u_j);
            v = v - proy_coef * u_j;
        end

        % Normalizar la matriz resultante
        norm_v = norma_matriz(v);

        if norm_v > 1e-10 % Evitar división por cero
            base_ortonormal{i} = v / norm_v;
        else
            error('La base no es linealmente independiente');
        end
    end
end

% ============================================
% EJEMPLO DE USO
% ============================================

% Definir tu base aquí (ejemplo con la base estándar)
% Puedes modificar estas matrices con tu base personalizada
base_original = {
    [1 0; 0 1],  % E11
    [1 1; 0 0],  % E12
    [1 0; 1 1],  % E21
    [1 1; 1 1]   % E22
};

% Calcular base ortonormal
base_ortonormal = gram_schmidt_matrices(base_original);

% Mostrar resultados
fprintf('\n=== BASE ORTONORMAL CALCULADA ===\n\n');
for i = 1:length(base_ortonormal)
    fprintf('Matriz %d:\n', i);
    disp(base_ortonormal{i});

    % Verificar ortonormalidad
    fprintf('Norma: %f\n', norma_matriz(base_ortonormal{i}));

    % Verificar ortogonalidad con las anteriores
    for j = 1:i-1
        prod = producto_interno(base_ortonormal{i}, base_ortonormal{j});
        fprintf('Producto con matriz %d: %e\n', j, prod);
    end
    fprintf('------------------------\n\n');
end

% Verificar que la base es ortonormal
fprintf('\n=== VERIFICACIÓN DE ORTONORMALIDAD ===\n');
for i = 1:length(base_ortonormal)
    for j = 1:length(base_ortonormal)
        prod = producto_interno(base_ortonormal{i}, base_ortonormal{j});
        fprintf('(%d,%d): %e\t', i, j, prod);
        if i == j
            % Debería ser aproximadamente 1
            if abs(prod - 1) > 1e-10
                fprintf(' ¡ERROR! Debería ser 1\n');
            end
        else
            % Debería ser aproximadamente 0
            if abs(prod) > 1e-10
                fprintf(' ¡ERROR! Debería ser 0\n');
            end
        end
    end
    fprintf('\n');
end
