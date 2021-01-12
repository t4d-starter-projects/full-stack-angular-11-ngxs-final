import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';

import { ChangePasswordForm } from '../../models/ChangePasswordForm';
import { confirmValue } from '@t4d-wnow/shared-lib';

@Component({
  selector: 'app-change-password-form',
  templateUrl: './change-password-form.component.html',
  styleUrls: ['./change-password-form.component.css']
})
export class ChangePasswordFormComponent implements OnInit {

  @Output()
  changePassword = new EventEmitter<ChangePasswordForm>();

  changePasswordForm!: FormGroup;

  constructor(private fb: FormBuilder) { }

  ngOnInit(): void {
    this.changePasswordForm = this.fb.group({
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
    }, { validators: [confirmValue('newPassword', 'confirmPassword')] });
  }

  public doChangePassword() {
    if (this.changePasswordForm.valid) {
      this.changePassword.emit(this.changePasswordForm.value);
    }
  }

}
