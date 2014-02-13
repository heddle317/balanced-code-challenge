drop table if exists images;
create table images (
    id integer primary key autoincrement,
    name text not null,
    image text not null
);
