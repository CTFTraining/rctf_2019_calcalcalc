# RCTF 2019 calcalcalc

## 题目详情

- RCTF 2019 calcalcalc
- It's an unbreakable and reliable calculator... I think.

## 考点

- nodejs code
- bodyParser
- Unintended solution is timing attack
- **No intended solution... So this challenge will be reused XD**

## 启动

	docker-compose up -d
	open http://127.0.0.1:8082/

### Writeups

- [calcalcalc](https://github.com/zsxsoft/my-ctf-challenges/blob/master/rctf2019/calcalcalc/readme.md)

## 复现说明及修改

该环境根据开源代码[calcalcalc](https://github.com/zsxsoft/my-ctf-challenges/tree/master/rctf2019/calcalcalc)搭建

- 重构 Dockerfile - 精简化
- 移除针对生产环境的各种配置
- alpine 万岁

## 版权

该题目复现环境尚未取得主办方及出题人相关授权，如果侵权，请联系本人<virink@outlook.com>删除
(出题人快来 PR 掉这个, 此处@zsxsoft )
