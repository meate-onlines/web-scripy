# web-scripy
scrapy爬虫框架学习交流

#Require

python == 3.6

scrapy == 2.4.0

requests == 2.24.0

PyMySQL == 0.10.1

Redis == 3.2.0

#SQL

```CREATE TABLE `proxy_ip` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) COLLATE utf8_croatian_ci NOT NULL DEFAULT '0',
  `port` varchar(255) COLLATE utf8_croatian_ci NOT NULL DEFAULT '0',
  `speed` float(10,5) NOT NULL,
  `proxy_type` varchar(255) COLLATE utf8_croatian_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;```

```CREATE TABLE `xuexila_article` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_croatian_ci NOT NULL DEFAULT '' COMMENT '文章标题',
  `keywords` varchar(255) COLLATE utf8_croatian_ci NOT NULL DEFAULT '' COMMENT '文章关键字',
  `description` varchar(255) COLLATE utf8_croatian_ci NOT NULL DEFAULT '' COMMENT '文章描述',
  `content_text` longtext COLLATE utf8_croatian_ci NOT NULL COMMENT '文章内容',
  `html` varchar(125) COLLATE utf8_croatian_ci NOT NULL DEFAULT '' COMMENT '文件名',
  `url` varchar(125) COLLATE utf8_croatian_ci NOT NULL DEFAULT '' COMMENT '链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3934 DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;```

#WARING
本项目所有的源代码和数据仅仅用于学习交流使用,禁止用于商业目的.如有违反,后果自负!

