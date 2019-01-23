from scrapy import cmdline
name='51job'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())




# from scrapy import cmdline
#
# command='scrapy crawl bizhi'
# cmdline.execute(command.split())