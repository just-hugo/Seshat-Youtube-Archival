from archivenow import archivenow
import archiveis

# megalodon.jp
# archivenow.push("https://www.nytimes.com/2021/10/28/climate/climate-change-framework-bill.html","--all")

archive_url = archiveis.capture("https://www.nytimes.com/2021/10/28/climate/climate-change-framework-bill.html")

print(archive_url)