import copy

li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print(li1[i],end=" ")

li2[2][0] = 7

print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print(li2[i],end=" ")

print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print(li1[i],end=" ")

# use id to find the address

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
str_1='Lorem ipsum dolor sit amet, consectetur adipiscing eli . Duis auctor facilisis sapien, ut congue lorem ultrices eget. Aenean sit amet lobortis quam. Quisque ornare quis lacus a auctor. Vivamus porta rhoncus quam, in sollicitudin nibh tempus sed. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum et varius purus. Praesent vehicula libero eu augue viverra, ac bibendum neque pellentesque. Nulla bibendum, nulla vitae varius elementum, velit arcu euismod nibh, nec dapibus velit diam et sapien. Nulla sed sapien et orci sagittis vestibulum. Nam luctus nulla vulputate felis ornare, a iaculis ipsum ornare. Sed sed porta augue. Vestibulum lacus mauris, finibus vitae diam id, aliquet convallis magna. Fusce ornare, lorem a viverra facilisis, tellus libero rutrum ante, ut congue augue mi at nibh. Nam metus quam, ultricies eu nisi quis, eleifend suscipit massa. Nullam tristique quam est, eu tempus sem egestas efficitur. Sed rutrum ut dui non bibendum.Ut dapibus interdum rhoncus. Nam vulputate venenatis orci non auctor. Vivamus consectetur purus ac enim viverra, id faucibus risus pretium. Nam tortor ligula, faucibus vitae ante nec, efficitur tempor odio. Nullam iaculis magna purus, et sodales tortor ultricies non. Proin ut porttitor orci. Morbi vehicula justo odio, ut sodales quam ultrices non. Aliquam quis gravida nunc. Donec et neque lectus. Nulla gravida nibh erat, ut commodo ante lobortis id. Maecenas odio tellus, interdum vitae aliquam eu, lobortis ac odio. Integer mattis sapien vel orci placerat, at molestie arcu cursus. Pellentesque sit amet diam ligula. Donec pellentesque id mauris eu semper. Donec lectus risus, congue in ex non, blandit iaculis massa. Sed auctor, erat ac interdum dignissim, elit dolor condimentum risus, ac mollis libero nisi eget ante. Nullam at elit urna. Vivamus mollis ligula a imperdiet congue. Suspendisse auctor tincidunt erat in sagittis. Morbi tempor diam at nibh dapibus, quis accumsan quam gravida. Integer vehicula finibus enim. Phasellus eu fermentum augue, vel luctus elit. Aenean dictum libero interdum nulla mattis auctor. Aliquam nec suscipit tellus, id euismod tortor. Nunc nec ligula arcu. Donec sapien nibh, consequat pellentesque tortor sit amet, molestie aliquam arcu. Sed convallis lectus nec nunc molestie, nec maximus quam scelerisque. Etiam viverra eros a placerat volutpat. Phasellus facilisis metus quam, quis suscipit erat interdum at.In suscipit ac purus ut cursus. Sed sollicitudin est at felis sagittis, non accumsan elit tempor. Ut vitae augue vel nisl ultrices dapibus. Morbi feugiat felis eu velit tristique, quis dignissim sem ornare. Aliquam quis dictum ipsum, et cursus turpis. Pellentesque ac dolor sit amet quam malesuada dictum. Phasellus nunc velit, lacinia nec turpis ut, congue auctor massa. Sed varius, lorem id bibendum placerat, orci lectus mattis mi, non iaculis dui eros eu elit. Nam porttitor lacus ac orci egestas rhoncus. Morbi malesuada eros purus, quis fermentum velit dapibus id. Pellentesque ac tincidunt justo, eget mollis nulla. Praesent vel ultricies mi, a tincidunt eros. Vivamus viverra blandit leo, non aliquet lorem.'