DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    link TEXT NOT NULL,
    sizes_available TEXT,
    size_selected TEXT,
    shahremun_link text,
    barcode text,
    price int,
    sales_price int,
    title text,
    slug text,
    product_color text,
    image_name text,
    image_alt text,
    image_list text,
    gharanti text,
    supplier text,
    descriptions text,
    image_string text

);


