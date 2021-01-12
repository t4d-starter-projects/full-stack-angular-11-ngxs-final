import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { LoginForm } from '../../models/LoginForm';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.css']
})
export class LoginFormComponent implements OnInit {

  loginForm!: FormGroup;
  loginFormSubmitted = false;

  @Output()
  login = new EventEmitter<LoginForm>();

  @Output()
  clear = new EventEmitter<void>();

  get showLoginFormValidationSummary() {
    return this.loginForm.invalid && this.loginFormSubmitted;
  }

  get showUsernameError() {
    const usernameFormControl = this.loginForm.get('username');
    return usernameFormControl!.invalid;
  }

  get showPasswordError() {
    const passwordFormControl = this.loginForm.get('password');
    return passwordFormControl!.invalid;
  }

  constructor(private fb: FormBuilder) { }

  // username: 'adodsworth'
  // password: 'testpass'

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      username: ['adodsworth', { validators: [Validators.required] }],
      password: ['testpass', { validators: [Validators.required] }],
    });
  }

  doLogin(): void {
    this.loginFormSubmitted = true;
    if (this.loginForm.invalid) return;
    this.login.emit(this.loginForm!.value);
  }

  doClear(): void {
    this.loginForm!.reset();
    this.clear.emit();
  }

}
