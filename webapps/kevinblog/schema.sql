drop table if exists posts;
create table posts(
    ID int auto_increment,
    primary key (id),
    date text not null,
    title text not null,
    body text not null
);
