

               normalize=False, range=None, scale_each=False, pad_value=0):
    grid = vutils.make_grid(tensor, nrow=nrow, padding=padding, 
                            normalize=normalize, range=range, 
                            scale_each=scale_each, pad_value=pad_value)
    ndarr = grid.mul(255).add(0.5).clamp(0, 255).byte().permute(1, 2, 