import { FormGroup } from '@angular/forms';

export const confirmValue = (firstControlName: string, secondControlName: string) =>
  (formGroup: FormGroup) => {

    const firstControl = formGroup.get(firstControlName);
    const secondControl = formGroup.get(secondControlName);

    if (firstControl?.value !== secondControl?.value) {
      return {
        confirmValue: {
          firstControlName,
          firstControlValue: firstControl?.value,
          secondControlName,
          secondControlValue: secondControl?.value,
        }
      };
    }

    return null;
  };