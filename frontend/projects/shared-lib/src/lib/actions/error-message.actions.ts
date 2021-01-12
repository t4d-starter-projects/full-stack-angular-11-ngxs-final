

export class SetErrorMessage {
  static readonly type = '[App] Set Error Message';
  constructor(public errorMessage: string) { }
}

export class ClearErrorMessage {
  static readonly type = '[App] Clear Error Message';
}