# D. The Model Registry (Medium)
# Problem statement
# The lab keeps a registry of models. If nobody mentions a learning rate, the senior’s rule is: use 0.01. “If you forget lr, the default will remember for you.”
# Write model_info(name, layers, lr=0.01) that returns:
# Model: <name>, Layers: <layers>, LR: <lr>
# Today there are t registration requests.
# Type 1 — intern is lazy: only name and layers. Use the default lr. Call with positional arguments.
# Type 2 — intern typed fields in a weird order. Call with keyword arguments (layers=..., name=...).
# Type 3 — intern is brave and sets a custom learning rate.
# Print the registry line for each request.
# Input
# First line: integer t (1 ≤ t ≤ 10).
# Each of the next t lines:
# 1 name layers   or   2 name layers   or   3 name layers lr
# Output
# t registry lines.
# Example
# Input
# 3
# 1 TinyNet 3
# 2 ResNet 5
# 3 FastNet 2 0.001
# Output
# Model: TinyNet, Layers: 3, LR: 0.01
# Model: ResNet, Layers: 5, LR: 0.01
# Model: FastNet, Layers: 2, LR: 0.001


def model_info(name, layers, lr=0.01):
    return print(f"Model: {name}, Layers: {layers}, LR: {lr}")



t=int(input())
while(t>0):
    t-=1
    inp=input().split()
    typ=int(inp[0])
    model=inp[1]
    lyr=inp[2]
    
    if(typ==1):
        model_info(model,lyr)
    elif(typ==2):
        model_info(layers=lyr,name=model)
    else:
        lr=float(inp[3])
        model_info(model,lyr,lr)


