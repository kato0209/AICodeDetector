FloatingActionButton fabButton = new FloatingActionButton.Builder(this)
       .withDrawable(getResources().getDrawable(R.drawable.ic_action_add))
     .withTitle("Add item to collection")
    	.withTitle("")
       .withMenu(true)  .withButtonColor(Color.WHITE)
        .withGravity(Gravity.BOTTOM | Gravity.RIGHT)
       .withMargins(0, 0, 16, 16)
        .create();