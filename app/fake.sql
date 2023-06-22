insert into app_specialize(specialize_id, specialize_name, academy_name) values (1,"计算机科学与技术","计算机科学与工程学院"),
                               (2, "软件工程","计算机科学与工程学院"),
                               (3,"网络安全","计算机科学与工程学院"),
                               (4, "网络工程","计算机科学与工程学院"),
                               (5, "社会工作", "政法学院"),
                               (6, "法律与社会","政法学院"),
                               (7, "大数据分析","数学与统计学院"),
                               (8,"服装设计","服装设计学院"),
                               (9, "网络与新媒体","文学传达学院"),
                               (10,"艺术鉴赏","艺术学院");

select * from app_specialize

delete from app_contact where specialize_id = 0;

select * from app_contact where address like '%广东%';

select * from app_contact

select * from app_user;

delete from app_user where sid = 8;

delete from app_user;

update app_user set identity = 0 where sid = 1;

insert into app_user value (null, 'admin', '13790841230', '1', '123456');

delete from app_contact