
    args = parser.parse_args()
    path = get_settings_path()

    if args.default:
        if populate_settings_dir(force=True):
            print(f'Populated {path} with default settings files')
        else:
            print(f'{path} is already a default settings directory')
    else:
        print(f'Current DeepPavlov settings path: {path}')