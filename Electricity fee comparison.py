unit_price={"normal":0.5469,"top":0.5769,"bottom":0.3469}
kwh={"standard":0.69,"drying":1.05}

for k,v in unit_price.items():
    print("Standard ",k,":",round(kwh["standard"]*v,2))
    print("Drying ",k,":",round(kwh["drying"]*v*2,2))
    print("Total: Wash 1 hrs + Dry 2 hrs")
    print("\t",round(kwh["standard"]*v+kwh["drying"]*v*2,2))
