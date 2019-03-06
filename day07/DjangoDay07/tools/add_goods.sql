delimiter //
create procedure add_goods(num int(4))
begin
    # 定义变量
    declare _i,_price,_temp int(4) default 0;
    declare _name,_icon,_detail varchar(255) default '';
    declare BASE_PATH varchar(255) default '/static/img/';

    # 循环
    while _i<num do
        # 设置变量
        set _temp = round(rand()*10000+1000);
        set _name = concat(_temp,'-商品名称');
        set _temp = round(rand()*5+1);
        case _temp
        when 1 then
            set _icon = concat(BASE_PATH,'1.jpg');
        when 2 then
            set _icon = concat(BASE_PATH,'2.jpg');
        when 3 then
            set _icon = concat(BASE_PATH,'3.jpg');
        when 4 then
            set _icon = concat(BASE_PATH,'4.jpg');
        when 5 then
            set _icon = concat(BASE_PATH,'5.jpg');
        when 6 then
            set _icon = concat(BASE_PATH,'6.jpg');
        else
            set _icon = concat(BASE_PATH,'1.jpg');
        end case;
        set _temp = round(rand()*10000+1000);
        set _price = _temp;
        set _temp = round(rand()*10000+1000);
        set _detail = concat(_temp,'-Apple/苹果 iPhone 7 Plus苹果7代7pluss国行美版三网5.5寸7p手机');

        # 插入数据
        insert into goods(name,icon,price,detail) value(_name,_icon,_price,_detail);

        # 修改次数
        set _i = _i + 1;
    end while;

    # 显示数据
    select * from goods;
end
//
delimiter ;
