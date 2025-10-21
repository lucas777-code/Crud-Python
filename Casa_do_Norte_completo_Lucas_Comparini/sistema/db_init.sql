-- Ativa a verificação de integridade referencial
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS usuarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  usuario TEXT UNIQUE,
  senha TEXT,
  nome_completo TEXT
);

CREATE TABLE IF NOT EXISTS comidas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo TEXT UNIQUE,
  nome TEXT,
  descricao TEXT,
  categoria TEXT,
  origem TEXT,
  ingredientes TEXT,
  porcao TEXT,
  calorias REAL,
  quantidade INTEGER DEFAULT 0,
  estoque_minimo INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS movimentacoes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  comida_id INTEGER,
  usuario_id INTEGER,
  tipo TEXT,
  quantidade INTEGER,
  data TEXT,
  observacao TEXT,
  FOREIGN KEY(comida_id) REFERENCES comidas(id),
  FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

INSERT OR IGNORE INTO usuarios (usuario, senha, nome_completo) VALUES
('admin', '123', 'Administrador'),
('helena', '123', 'Helena Silva'),
('ravi', '123', 'Ravi Santos');

INSERT OR IGNORE INTO comidas (codigo, nome, descricao, categoria, origem, ingredientes, porcao, calorias, quantidade, estoque_minimo) VALUES
('C001', 'Baião de Dois', 'Arroz com feijão verde, queijo coalho e carne seca.', 'Prato Principal', 'Ceará', 'Arroz, feijão, queijo coalho, carne seca', '300g', 480, 15, 3),
('C002', 'Carne de Sol com Macaxeira', 'Carne de sol acebolada com macaxeira frita.', 'Prato Principal', 'Nordeste', 'Carne de sol, macaxeira, cebola roxa, manteiga de garrafa', '450g', 700, 25, 8),
('C003', 'Vatapá', 'Creme de pão com camarão seco e azeite de dendê.', 'Acompanhamento', 'Bahia', 'Pão, camarão seco, leite de coco, azeite de dendê', '250g', 450, 18, 6);

INSERT OR IGNORE INTO movimentacoes (comida_id, usuario_id, tipo, quantidade, data, observacao) VALUES
(1, 1, 'entrada', 5, '2025-10-01', 'Reposição de estoque'),
(2, 2, 'saída', 2, '2025-10-02', 'Venda teste'),
(3, 3, 'entrada', 10, '2025-10-03', 'Novo lote recebido');
