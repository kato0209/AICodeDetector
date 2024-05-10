
  fig = plt.figure(figsize=(4, 4))
  canvas = backend_agg.FigureCanvasAgg(fig)

  for i, image in enumerate(images):
    ax = fig.add_subplot(4, 4, i + 1)
    plt.axis('off')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.imshow(image.reshape(IMAGE_SHAPE[:-1]), cmap='Greys_r')

  fig.tight_layout()
  plt.subplots_adjust(wspace=0.05, hspace=0.05)
  canvas.print_figure(fname, format='png')